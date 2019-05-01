<?php

$file = 'myjson';

$db = new PDO('sqlite:datalogger.db');

$temp = $db->query('SELECT * FROM pidata');

$temp->setFetchMode(PDO::FETCH_ASSOC);

$sample = array();

while($row = $temp->fetch()) {

  extract($row);

  $sample[] = array($Date, $Time, floatval($TEMP1), $IR, $FULL, $VIS, $LUX, floatval($TEMP2), floatval($PRESSURE), floatval($HUMID));
}

$data = json_encode($sample);

file_put_contents($file, $data);

?>

