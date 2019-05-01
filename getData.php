// This script is for taking the data from the database and formating it in json
// so it can be red by the chartJS script
<?php


$db = new PDO('sqlite:datalogger.db');

$temp = $db->query('SELECT * FROM pidata DESC LIMIT 1440');

$temp->setFetchMode(PDO::FETCH_ASSOC);

$sample = array();

while($row = $temp->fetch()) {

  extract($row);

  $sample[] = array($Date, $Time, $TEMP1, $IR, $FULL, $VIS, $LUX, $TEMP2, $PRESSURE, $HUMID);
}

$data = json_encode($sample);
# file_put_contents($file, "data1");
# file_put_contents($file, $data);

?>

