var mainOptions = document.querySelectorAll('.mainOption');

// Adding an event listener to each element with the class "mainOption"
for (var i = 0; i < mainOptions.length; i++) {
    mainOptions[i].addEventListener("click", function(event) {
        // Showing or hiding the "option-list" that is a direct child of the clicked "mainOption"
        var optionsList = this.parentElement.querySelector('.option-list');
        if (optionsList) {
            if (optionsList.style.display === 'block') {
                optionsList.style.display = 'none';
            } else {
                optionsList.style.display = 'block';
            }
        }

        // Stop the event propagation to prevent the document click event from being triggered immediately
        event.stopPropagation();
    });
}

// Adding an event listener to each element with the class "option"
var optionElements = document.querySelectorAll('.option');
for (var i = 0; i < optionElements.length; i++) {
    optionElements[i].addEventListener("click", function() {
        // Changing the text in the parent "mainOption" to the text of the clicked "option"
        var mainOption = this.closest('.parent-list').querySelector('.mainOption');
        mainOption.textContent = this.textContent;

        // Hiding the "option-list" after a click
        var optionsList = this.closest('.option-list');
        if (optionsList) {
            optionsList.style.display = 'none';
        }
    });
}

// Adding a document click event listener to close the "option-list" on a click outside of it
document.addEventListener("click", function() {
    var allOptions = document.querySelectorAll('.option-list');
    for (var j = 0; j < allOptions.length; j++) {
        allOptions[j].style.display = 'none';
    }
});
