function bindEmailCaptchaClick(){
    $("#captcha-btn").click(function (event){
        // $this: represents the jquery object of the current button
        var $this = $(this);
        // Blocking default events
        event.preventDefault();
        var email = $("input[name='email']").val();
        $.ajax({
            // http://127.0.0.1:5000
            // /auth/captcha/email?email=xx@gmail.com
            url: "/auth/captcha/email?email="+email,
            method: "GET",
            success: function(result){
                var code = result['code'];
                if(code == 200){
                    var countdown = 60;
                    // Cancel the button click event before the countdown starts
                    $this.off("click");
                    var timer = setInterval(function(){
                        $this.text(countdown);
                        countdown -= 1;
                        // Execute at the end of the countdown
                        if(countdown <= 0){
                            // Clear the timer
                            clearInterval(timer);
                            // Change the text of the button back again
                            $this.text("Get verification code");
                            // Rebinding click events
                            bindEmailCaptchaClick();
                        }
                    }, 1000);
                    alert("Email verification code sent successfully!")
                } else {
                    alert(result['message']);
                }
            },
            fail: function(error){
                console.log(error);
            }
        })
    });
}

// Execute after the entire page has loaded
$(function (){
    bindEmailCaptchaClick()
});