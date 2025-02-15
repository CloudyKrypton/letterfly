///// Login

function validateLogin() {
    // Get the values from the input fields
    var username = document.getElementById("username").value;
    var password = document.getElementById("password").value;
  
    // Check if the fields are empty
    if (username === "" || password === "") {
      alert("Please fill in both fields.");
      return;
    }

    // Simulate a successful login (you could connect to a backend API here)
    if (username == "" || password == "") {
      // Redirect to a new page after successful login (optional)
      alert("Please fill in both fields.");
    } else {
      window.location.href = "/dashboard";
    }
}

document.getElementById("login").addEventListener("click", async function(event) {
  event.preventDefault();  // Prevent form from reloading the page

  const formData = {
      username: document.getElementById("username").value,
      password: document.getElementById("password").value,
  };

  try {
    const response = await fetch("http://127.0.0.1:5000/submit_login", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(formData)
    });

    const data = await response.json();
      if (data.status === "success") {
        console.log(data.message);  // Show success message
        window.location.href = "/dashboard";  // Redirect after successful signup
      } else {
          console.error("Login failed:", data.message);  // Handle error message
      }
    } catch (error) {
      console.error("Error:", error);
    }
});