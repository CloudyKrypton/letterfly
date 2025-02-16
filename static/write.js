let html = "";
let text = "";
let recipient = "";

function sendLetter() {
    html = quill.getSemanticHTML(0);
    text = quill.getText(0);
    console.log(text);

    window.location.href = "/send";
}

const friends = ["Rose", "Lily", "Daisy", "Iris", "Violet", "Robin", "Sparrow", "Wren",
    "Hawk", "Jasmine"]
  
function populateFriends(selectId) {
    const friendSelect = document.getElementById(selectId);
    
    // Clear any existing options (if needed, e.g. for reset)
    friendSelect.innerHTML = '<option value="" disabled selected>Select a friend</option>';
    
    // Loop through the array and create option elements dynamically
    friends.forEach(function(friend) {
      const option = document.createElement("option");
      option.value = friend;
      option.textContent = friend;
      friendSelect.appendChild(option);
    });
  }
  
  populateFriends("friend-choose");

  document.getElementById("send-friend-btn").addEventListener("click", function() {
    const friendSelect = document.getElementById("friend-choose");
    const friend = friendSelect.value;
  
    if (friend) {
      recipient = friend;
    } else if (!friend) {
      alert("Please choose a friend to send your letter to!");
    }
  });

  //////////////////////////////

  function enterUser() {
    // Get the values from the input fields
    var username = document.getElementById("username").value;
  
    // Check if the fields are empty
    if (username === "") {
      alert("Please enter a userID to send your letter to!");
      return;
    }

    recipient = username;
  
    // // Simulate a successful login (you could connect to a backend API here)
    // if (username === "admin") {
    //   // Redirect to a new page after successful login (optional)
    //   finalSend();
    // } else {
    //   alert("Invalid username.");
    // }
}

function openLetter() {
  recipient = "open";
}

document.getElementById("send-friend-btn").addEventListener("click", async function(event) {
  event.preventDefault();  // Prevent form from reloading the page

  const formData = {
      content: html,
      recipient: recipient
  };

  try {
    const response = await fetch("http://127.0.0.1:5000/submit_signup", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(formData)
    });

      const data = await response.json();
        if (data.status === "success") {
          console.log(data.message);  // Show success message
          finalSend();
        } else {
            console.error("Signup failed:", data.message);  // Handle error message
        }
      } catch (error) {
        console.error("Error:", error);
      }
});

document.getElementById("enter-user-btn").addEventListener("click", async function(event) {
  event.preventDefault();  // Prevent form from reloading the page

  const formData = {
      content: html,
      recipient: recipient
  };

  try {
    const response = await fetch("http://127.0.0.1:5000/submit_signup", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(formData)
    });

      const data = await response.json();
        if (data.status === "success") {
          console.log(data.message);  // Show success message
          finalSend();

        } else {
            console.error("Signup failed:", data.message);  // Handle error message
        }
      } catch (error) {
        console.error("Error:", error);
      }
});

document.getElementById("open-letter-btn").addEventListener("click", async function(event) {
  event.preventDefault();  // Prevent form from reloading the page

  const formData = {
      content: html,
      recipient: recipient
  };

  try {
    const response = await fetch("http://127.0.0.1:5000/submit_signup", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(formData)
    });

      const data = await response.json();
        if (data.status === "success") {
          console.log(data.message);  // Show success message
          finalSend();
        } else {
            console.error("Signup failed:", data.message);  // Handle error message
        }
      } catch (error) {
        console.error("Error:", error);
      }
});

function finalSend() {
  alert("Your letter has been sent!");
  window.location.href = "/dashboard";
}