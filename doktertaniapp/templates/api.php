<?php 
    require_once('connection.php');

    if (empty($_GET)) {
        $query = mysqli_query($connection, "SELECT * FROM saran_cabai");

        $result = array();
        while($row = mysqli_fetch_array($query)) {
            array_push( $result, array (
                'penyakit' => $row['penyakit'],
                'gejala_umum' => $row['gejala_umum']
            ) );
        }

        echo json_encode (
            array('result'=> $result)
        );

    } else {
        $penyakit = mysqli_real_escape_string($connection, $_GET['penyakit']);
        $query = mysqli_query($connection, "SELECT * FROM saran_cabai WHERE penyakit='$penyakit'");

        $result = array();
        while($row = $query -> fetch_assoc()) {
            $result = array (
                'gejala_umum' => $row['gejala_umum']
            );
        }

        echo json_encode (
            $result
        );
    }
?>
