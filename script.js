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
    if (username === "admin" && password === "password123") {
      // Redirect to a new page after successful login (optional)
      window.location.href = "dashboard.html";
    } else {
      alert("Invalid username or password.");
    }
}

// Array of languages (you can expand this array as needed)
const languagesArray = [
    "English", "Spanish", "French", "German", "Chinese", "Arabic", "Italian", 
    "Russian", "Portuguese", "Japanese", "Korean", "Hindi", "Dutch", "Swedish", 
    "Turkish", "Polish", "Greek", "Hebrew", "Romanian", "Hungarian", "Czech"
  ];
  
  // Function to populate the select dropdown with languages for both forms
  function populateLanguages(selectId) {
    const languageSelect = document.getElementById(selectId);
    
    // Clear any existing options (if needed, e.g. for reset)
    languageSelect.innerHTML = '<option value="" disabled selected>Select a language</option>';
    
    // Loop through the array and create option elements dynamically
    languagesArray.forEach(function(language) {
      const option = document.createElement("option");
      option.value = language;
      option.textContent = language;
      languageSelect.appendChild(option);
    });
  }
  
  // Call the function to populate the languages for both forms
  populateLanguages("language-read");
  populateLanguages("language-write");
  
  document.getElementById("add-language-read-btn").addEventListener("click", function() {
    const languageSelect = document.getElementById("language-read");
    const language = languageSelect.value;
  
    if (language && !isLanguageAdded(language, "read")) {
      addLanguageToList(language, "read");
      languageSelect.value = ""; // Reset select
    } else if (!language) {
      alert("Please select a language you read.");
    }
  });
  
  document.getElementById("add-language-write-btn").addEventListener("click", function() {
    const languageSelect = document.getElementById("language-write");
    const language = languageSelect.value;
  
    if (language && !isLanguageAdded(language, "write")) {
      addLanguageToList(language, "write");
      languageSelect.value = ""; // Reset select
    } else if (!language) {
      alert("Please select a language you write in.");
    }
  });
  
  function isLanguageAdded(language, formType) {
    const languageList = document.getElementById(`language-list-${formType}`);
    const languages = languageList.getElementsByTagName("li");
    
    for (let i = 0; i < languages.length; i++) {
      if (languages[i].textContent.trim() === language) {
        return true; // Language is already in the list
      }
    }
    return false;
  }
  
  function addLanguageToList(language, formType) {
    const languageList = document.getElementById(`language-list-${formType}`);
    
    const li = document.createElement("li");
    li.textContent = language;
    
    // Add a remove button next to the language
    const removeBtn = document.createElement("button");
    removeBtn.textContent = "Remove";
    removeBtn.onclick = function() {
      languageList.removeChild(li);
    };
    
    li.appendChild(removeBtn);
    languageList.appendChild(li);
  }