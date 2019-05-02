<?php

#This script is for taking the data from the database and formating it in json
#so it can be red by the chartJS script

$db = new SQLite3('datalogger.db');

$temp = $db->query('SELECT * FROM pidata DESC LIMIT 1440');

$sample = array();

while($row = $temp->fetchArray(SQLITE3_ASSOC)) {

#  extract($row);
#  $sample[] = array($Date, $Time, $TEMP1, $IR, $FULL, $VIS, $LUX, $TEMP2, $PRESSURE, $HUMID);
#  $jsonArray[] = $row;

  $storeData['t'] = $row['Time'];
  $storeData['y'] = $row['TEMP1'];
  $finalData['data1'][] = $storeData;
}
while($row = $temp->fetchArray(SQLITE3_ASSOC)) {
  $storeData['t'] = $row['Time'];
  $storeData['y'] = $row['IR'];
  $finalData['data2'][] = $storeData;
}
while($row = $temp->fetchArray(SQLITE3_ASSOC)) {
  $storeData['t'] = $row['Time'];
  $storeData['y'] = $row['FULL'];
  $finalData['data3'][] = $storeData;
}
while($row = $temp->fetchArray(SQLITE3_ASSOC)) {
  $storeData['t'] = $row['Time'];
  $storeData['y'] = $row['VIS'];
  $finalData['data4'][] = $storeData;
}
while($row = $temp->fetchArray(SQLITE3_ASSOC)) {
  $storeData['t'] = $row['Time'];
  $storeData['y'] = $row['LUX'];
  $finalData['data5'][] = $storeData;
}
while($row = $temp->fetchArray(SQLITE3_ASSOC)) {
  $storeData['t'] = $row['Time'];
  $storeData['y'] = $row['TEMP2'];
  $finalData['data6'][] = $storeData;
}
while($row = $temp->fetchArray(SQLITE3_ASSOC)) {
  $storeData['t'] = $row['Time'];
  $storeData['y'] = $row['PRESSURE'];
  $finalData['data7'][] = $storeData;
}
while($row = $temp->fetchArray(SQLITE3_ASSOC)) {
  $storeData['t'] = $row['Time'];
  $storeData['y'] = $row['HUMID'];
  $finalData['data8'][] = $storeData;
}


echo json_encode($finalData,JSON_PRETTY_PRINT);

?>

