function getCSRFToken() {   // from cookies
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // check if correct cookie
            if (cookie.substring(0, 'csrftoken'.length + 1) === ('csrftoken' + '=')) {
                cookieValue = decodeURIComponent(cookie.substring('csrftoken'.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

document.addEventListener('DOMContentLoaded', function() {
    var clickButton = document.getElementById('clickButton');
    var clickCountDisplay = document.getElementById('clickCount');

    // get counter value on page load
    var xhr = new XMLHttpRequest();
    xhr.open('GET', '/get_counter/');
    xhr.setRequestHeader('X-Requested-With', 'XMLHttpRequest');
    xhr.onload = function() {
        if (xhr.status === 200) {
            var response = JSON.parse(xhr.responseText);
            clickCountDisplay.textContent = response.counter;
        }
    };
    xhr.send();

    clickButton.addEventListener('click', function() {
        // ajax update counter
        var xhr = new XMLHttpRequest();
        xhr.open('POST', '/update_counter/');
        xhr.setRequestHeader('X-Requested-With', 'XMLHttpRequest');
        xhr.setRequestHeader('X-CSRFToken', getCSRFToken());
        xhr.onload = function() {
            if (xhr.status === 200) {
                var response = JSON.parse(xhr.responseText);
                clickCountDisplay.textContent = response.counter;
            }
        };
        xhr.send();
    });
});
