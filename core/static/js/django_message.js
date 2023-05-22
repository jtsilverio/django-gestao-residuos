document.addEventListener("DOMContentLoaded", function(){
    var element = document.getElementById("django-message");
    var elementBtn = document.getElementById("django-message-btn");

    // Create toast instance
    var djangoMessage = new bootstrap.Toast(element);
    elementBtn.addEventListener("click", function(){
        djangoMessage.hide();
    });
    
    djangoMessage.show();
});