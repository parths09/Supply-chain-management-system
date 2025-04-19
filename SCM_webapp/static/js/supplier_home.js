function toggleDetails(row) {
    const nextRow = row.nextElementSibling;
    if (nextRow && nextRow.classList.contains('details-row')) {
      nextRow.style.display = nextRow.style.display === 'table-row' ? 'none' : 'table-row';
    }
  }

function handleDeny(event, requestId, w_id) {
    event.stopPropagation(); // Prevent parent row click
    Swal.fire({
      title: 'Deny Request',
      text: 'Are you sure you want to deny this request?',
      icon: 'warning',
      showCancelButton: true,
      confirmButtonText: 'Yes, deny it',
      cancelButtonText: 'Cancel'
    }).then((result) => {
      if (result.isConfirmed) {
        fetch("{% url 'supplier_home' %}", {
          method: "POST",
          headers: {
            "X-CSRFToken": "{{ csrf_token }}",
            "Content-Type": "application/json"
          },
          body: JSON.stringify({
            action: "deny",
            request_id: requestId,
            warehouse_id: w_id
          })
        })
        .then(response => {
          if (!response.ok) throw new Error('Network error');
          return response.json();
        })
        .then(() => {
          Swal.fire("Denied!", "Request has been denied.", "info")
            .then(() => location.reload());
        })
        .catch(error => {
          Swal.showValidationMessage(`Request failed: ${error}`);
        });
      }
    });
  }

function handleAccept(event, requestId, productName, Quantity, w_id) {
    event.stopPropagation(); // Prevent row toggle

    const orderDate = new Date().toISOString().split('T')[0];

    Swal.fire({
      title: 'Accept Request',
      html: `
        <div class="swal-input-container">
          <label for="product-name">Product:</label>
          <input id="product-name" class="swal2-input" value="${productName}" readonly>

          <label for="quantity">Quantity:</label>
          <input id="quantity" class="swal2-input" value="${Quantity}" readonly>

          <label for="order-date">Order Date:</label>
          <input id="order-date" class="swal2-input" value="${orderDate}" readonly>

          <label for="delivery-date">Delivery Date:</label>
          <input id="delivery-date" type="date" class="swal2-input" required>
        </div>
      `,
      focusConfirm: false,
      showCancelButton: true,
      confirmButtonText: 'Accept',
      preConfirm: () => {
        const deliveryDate = document.getElementById('delivery-date').value;
        if (!deliveryDate) {
          Swal.showValidationMessage('Please select a delivery date.');
          return false;
        }
        if (new Date(deliveryDate) < new Date(orderDate)) {
          Swal.showValidationMessage('Invalid delivery date.');
          return false;
        }

        return fetch("{% url 'supplier_home' %}", {
          method: "POST",
          headers: {
            "X-CSRFToken": "{{ csrf_token }}",
            "Content-Type": "application/json"
          },
          body: JSON.stringify({
            quantity: Quantity,
            action: "accept",
            request_id: requestId,
            delivery_date: deliveryDate,
            order_date: orderDate,
            warehouse_id: w_id
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
        Swal.fire('Accepted!', 'The request has been accepted.', 'success')
          .then(() => location.reload());
      }
    });
  }