let html = "";
let text = "";

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
      finalSend();
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
  
    // Simulate a successful login (you could connect to a backend API here)
    if (username === "admin") {
      // Redirect to a new page after successful login (optional)
      finalSend();
    } else {
      alert("Invalid username.");
    }
}

function openLetter() { 
  finalSend();
}

function finalSend() {
  alert("Your letter has been sent!");
  window.location.href = "/dashboard";
}