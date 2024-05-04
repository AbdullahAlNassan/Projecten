<?php
if (isset($_GET["id"])) {
    $id = $_GET["id"];

    $servername = "localhost";
    $username = "root";
    $password = "";
    $database = "myshop";
    $port = 3308;


    $connection = new mysqli($servername, $username, $password, $database, $port);

    $sql = "DELETE FROM users WHERE id=$id";
    $connection->query($sql);
}

header("location: /myshop/index.php");
exit;
?>