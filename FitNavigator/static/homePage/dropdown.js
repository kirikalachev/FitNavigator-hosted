var isDropdownVisible = false;

function dropdown() {
    var buttons = document.querySelectorAll('.navButton');
    var img = document.querySelector('#img2');

    if (!isDropdownVisible) {
        buttons.forEach(function(button) {
            button.style.display = "block";
        });

        img.style.display = "block";
    } 
    
    else {
        buttons.forEach(function(button) {
            button.style.display = "none";
        });

        img.style.display = "none";
    }

 
    isDropdownVisible = !isDropdownVisible;
}

document.addEventListener('click', function(event) {
    var dropdownContainer = document.querySelector('#div');


    if (!dropdownContainer.contains(event.target)) {

        if (isDropdownVisible) {
            dropdown();
        }
    }
});
