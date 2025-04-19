// This file contains the JavaScript code for handling product management in a supplier's dashboard.
  
function isExistingProduct(name) {
    return existingNames.map(n => n.toLowerCase()).includes(name.trim().toLowerCase());
  }

  function openAddProductSwal() {
    // Create a container for our form
    const productFormHTML = `
      <div class="swal-form-container">
        <div class="swal-form-title">Select or Add Product</div>
        
        <div class="swal-form-field">
          <select id="product-select" style="width: 100%">
            <option value="">-- Search or select a product --</option>
            ${existingNames.map(name => `<option value="${name}">${name}</option>`).join('')}
          </select>
        </div>
        
        <div class="product-option-divider">
          <span>OR</span>
        </div>
        
        <button type="button" id="new-product-btn" class="new-product-btn">Add New Product</button>
      </div>
    `;
    
    Swal.fire({
      title: 'Add Product',
      html: productFormHTML,
      showConfirmButton: false,
      showCancelButton: true,
      cancelButtonText: 'Cancel',
      customClass: {
        container: 'swal-wide'
      },
      didOpen: () => {
        // Initialize Select2 for product selection
        setTimeout(() => {
          $('#product-select').select2({
            dropdownParent: $('.swal2-container'),
            width: '100%',
            placeholder: 'Search or select a product',
            allowClear: true
          }).on('change', function() {
            const selectedProduct = $(this).val();
            if (selectedProduct) {
              showExistingProductForm(selectedProduct);
            }
          });
        }, 100);
        
        // Setup new product button
        document.getElementById('new-product-btn').addEventListener('click', function() {
          showNewProductForm();
        });
      }
    });
  }

function showExistingProductForm(productName) {
    const existingProductFormHTML = `
      <div class="swal-form-container">
        <div class="swal-form-title">Add Existing Product</div>
        
        <div class="swal-form-field">
          <label for="product-name">Product Name:</label>
          <input id="product-name"  value="${productName}" readonly>
        </div>
        
        <div class="swal-form-field">
          <label for="product-price">Price:</label>
          <input type="number" id="product-price" step="0.01" min="0.01" placeholder="Enter price" required>
        </div>
      </div>
    `;
    
    Swal.fire({
      title: 'Add Existing Product',
      html: existingProductFormHTML,
      showCancelButton: true,
      confirmButtonText: 'Add Product',
      confirmButtonColor: '#2d89ef',
      customClass: {
        container: 'swal-wide'
      },
      preConfirm: () => {
        const price = document.getElementById('product-price').value;
        
        if (!price || isNaN(price) || Number(price) <= 0) {
          Swal.showValidationMessage("Please enter a valid price");
          return false;
        }
        return fetch("{% url 'supplier_products' %}", {
          method: "POST",
          headers: {
            "X-CSRFToken": "{{ csrf_token }}",
            "Content-Type": "application/json"
          },
          body: JSON.stringify({
            action: "exist_add",            // corrected action
            name: productName,               // use the passed-in variable
            price: price
          })
        })
        .then(response => {
          if (!response.ok) throw new Error('Network error');
          return response.json();
        })
        .catch(error => {
          Swal.showValidationMessage(`Request failed: ${error}`);
        });
      }
    }).then(result => {
      if (result.isConfirmed) {
        Swal.fire({
          title: 'Success!',
          text: 'Product has been added.',
          icon: 'success',
          confirmButtonColor: '#2d89ef'
        }).then(() => location.reload());
      }
    });
  }

function showNewProductForm() {
    const newProductFormHTML = `
      <div class="swal-form-container">
        <div class="swal-form-title">Add New Product</div>
        
        <div class="swal-form-field">
          <label for="new-product-name">Product Name:</label>
          <input type="text" id="new-product-name" placeholder="Enter product name" required>
        </div>
        
        <div class="swal-form-field">
          <label for="new-product-description">Description:</label>
          <textarea id="new-product-description" placeholder="Enter product description"></textarea>
        </div>
        
        <div class="swal-form-field">
          <label for="new-product-price">Price:</label>
          <input type="number" id="new-product-price" step="0.01" min="0.01" placeholder="Enter price" required>
        </div>
        
        <div class="swal-form-field">
          <label for="new-product-category">Category:</label>
          <input type="text" id="new-product-category" placeholder="Enter category">
        </div>
      </div>
    `;
    
    Swal.fire({
      title: 'Add New Product',
      html: newProductFormHTML,
      showCancelButton: true,
      confirmButtonText: 'Add Product',
      confirmButtonColor: '#2d89ef',
      customClass: {
        container: 'swal-wide'
      },
      preConfirm: () => {
        const name = document.getElementById('new-product-name').value;
        const price = document.getElementById('new-product-price').value;
        
        if (!name || !name.trim()) {
          Swal.showValidationMessage("Please enter a product name");
          return false;
        }
        
        if (!price || isNaN(price) || Number(price) <= 0) {
          Swal.showValidationMessage("Please enter a valid price");
          return false;
        }
        if (isExistingProduct(name)) {
          Swal.showValidationMessage("Product already exists");
          return false;
        }
        // Check if the product name already exists
        return fetch("{% url 'supplier_products' %}", {
          method: "POST",
          headers: {
            "X-CSRFToken": "{{ csrf_token }}",
            "Content-Type": "application/json"
          },
          body: JSON.stringify({
            action: "new_add",            // corrected action
            name: name,               // use the passed-in variable
            price: price,
            description: document.getElementById('new-product-description').value,
            category: document.getElementById('new-product-category').value
          })
        })
        .then(response => {
          if (!response.ok) throw new Error('Network error');
          return response.json();
        })
        .catch(error => {
          Swal.showValidationMessage(`Request failed: ${error}`);
        });
      }
    }).then(result => {
      if (result.isConfirmed) {
        Swal.fire({
          title: 'Success!',
          text: 'Product has been added.',
          icon: 'success',
          confirmButtonColor: '#2d89ef'
        }).then(() => location.reload());
      }
    });
  }
function handleEdit(event,product_id, price, productName) {
    Swal.fire({
      title: 'Edit Product Price',
      html: `
        <div class="swal-input-container">
          <label for="product-name">Product:</label>
          <input id="product-name" class="swal2-input" value="${productName}" readonly>
  
          <label for="price">Enter Price:</label>
          <input class="swal2-input" type="number" name="price" id="price" step="0.01" min="0.01" value="${price}" required>
        </div>
      `,
      focusConfirm: false,
      showCancelButton: true,
      confirmButtonText: 'Confirm',
      preConfirm: () => {
        const newPrice = document.getElementById('price').value;
  
        if (!newPrice || isNaN(newPrice) || Number(newPrice) <= 0) {
          Swal.showValidationMessage("Please enter a valid price.");
          return false;
        }
  
        return fetch("{% url 'supplier_products' %}", {
          method: "POST",
          headers: {
            "X-CSRFToken": "{{ csrf_token }}",
            "Content-Type": "application/json"
          },
          body: JSON.stringify({
            product_id: product_id,
            price: newPrice,
            action: "edit",
          })
        }).then(response => {
          if (!response.ok) throw new Error('Network error');
          return response.json();
        }).catch(error => {
          Swal.showValidationMessage(`Request failed: ${error}`);
        });
      }
    }).then((result) => {
      if (result.isConfirmed) {
        Swal.fire('Done!', 'The price has been updated.', 'success')
          .then(() => location.reload());
      }
    });
  }
  
  
function handleDelete(event, product_id) {
    event.stopPropagation(); // Prevent parent row click
    Swal.fire({
      title: 'Delete Request',
      text: 'Are you sure you want to delete this product?',
      icon: 'warning',
      showCancelButton: true,
      confirmButtonText: 'Yes, delete it ',
      cancelButtonText: 'Cancel'
    }).then((result) => {
      if (result.isConfirmed) {
        fetch("{% url 'supplier_products' %}", {
          method: "POST",
          headers: {
            "X-CSRFToken": "{{ csrf_token }}",
            "Content-Type": "application/json"
          },
          body: JSON.stringify({
            action: "delete",
            product_id: product_id
          })
        })
        .then(response => {
          if (!response.ok) throw new Error('Network error');
          return response.json();
        })
        .then(() => {
          Swal.fire("Deleted!", "Product has been deleted", "info")
            .then(() => location.reload());
        })
        .catch(error => {
          Swal.showValidationMessage(`Request failed: ${error}`);
        });
      }
    });
  }