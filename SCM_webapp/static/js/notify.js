document.addEventListener("DOMContentLoaded", function () {
    const button = document.getElementById("notification-button");
    const dropdown = document.getElementById("notification-dropdown");

    button.addEventListener("click", () => {
      dropdown.style.display = (dropdown.style.display === "block") ? "none" : "block";
    });

    document.addEventListener("click", function (e) {
      if (!button.contains(e.target) && !dropdown.contains(e.target)) {
        dropdown.style.display = "none";
      }
    });
  });