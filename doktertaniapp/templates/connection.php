<?php

    define('HOST', 'localhost');
    define('USER', 'root');
    define('PASS', '');
    define('DB', 'datg1717_doktertani');

    $connection = mysqli_connect(HOST, USER, PASS, DB) or die
    ('Unable Connect');

?>