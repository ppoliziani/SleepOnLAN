<!DOCTYPE html>
<html lang="en" dir="ltr">
<head>
    <meta charset="UTF-8">
    <title>Script test</title>
</head>
<body>
    <h1>Page reload should show danington</h1>
    <?php
        $python = `python test.py`;
        print($python);
       ?>

</body>
</html>