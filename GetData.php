<?php

$servername = "WP12489468.SERVER-HE.DE";
$username = "dbu12519951";
$password = "HB248db%2";
$database = "db12519951-sprecherdatenbank";
$host = "localhost";


// https://dbadmin.hosteurope.de/phpmyadmin/db_structure.php?server=1&db=db12519951-sprecherdatenbank

// Erstelle Verbindung
$conn = new mysqli($host, $username, $password, $database);

// Verbindung prüfen
if ($conn->connect_error) {
        die ("Verbindung fehlgeschlagen: " . $conn->connect_error);
}
// echo "Verbindung erfolgreich \n";

$sql = "SELECT id, nachname, vorname, geschlecht, geburtsjahr, strasse, hausnummer, postleitzahl, stadt, bildlink, divers, personOfColor, emailadresse, telefonnummer, mindesthonorar,
                honorarkategorie, von01, bis01,
                von02, bis02,

                hoerprobe01,
                hoerprobe02,
                hoerprobe03,

                sa_kind,
                sa_teenager,
                sa_jungeerwachsen,
                sa_bestejahre,
                sa_seniorin,


                sc_sonor,
                sc_klar,
                sc_rauh,
                sc_weich,


                sk_deutsch,
                sk_englischgb,
                sk_englischus,
                sk_frz,
                sk_ital,

                sk_nied,
                sk_pol,
                sk_portu,
                sk_russ,
                sk_span,

                sk_tuerk,


                dl_bayerisch,
                dl_berlinerisch,
                dl_fraenkisch,
                dl_hessisch,
                dl_norddeutsch,

                dl_rheinisch,
                dl_saechsisch,
                dl_schwaebisch,
                dl_badisch,
                dl_schweizerdeutsch,

                dl_westfaelisch,
                dl_wienerisch,

                sl_hoch,
                sl_mittel,
                sl_tief,

                ge_sachbuch,
                ge_krimi,
                ge_belle,
                ge_erotik,

                hp_beschreibung1,
                hp_beschreibung2,
                hp_beschreibung3


FROM sprecherinnen";

$result = $conn->query($sql);

if ($result->num_rows > 0) 
        {
        // output data of each row
        while ($row = $result->fetch_assoc()) 
                {
                        echo "" . $row["id"]. "\n";
                        echo "" . $row["nachname"]. "\n";
                        echo "" . $row["vorname"]. "\n"; 
                        echo "" . $row["geschlecht"]. "\n"; 
                        echo "" . $row["geburtsjahr"]. "\n";
                        echo "" . $row["strasse"]. "\n"; 
                        echo "" . $row["hausnummer"]. "\n";  
                        echo "" . $row["postleitzahl"]. "\n";  
                        echo "" . $row["stadt"]. "\n";
                        echo "" . $row["bildlink"]. "\n";

                        echo "" . $row["divers"]. "\n";
                        echo "" . $row["personOfColor"]. "\n";

                        echo "" . $row["emailadresse"]. "\n";
                        echo "" . $row["telefonnummer"]. "\n";

                        echo "" . $row["mindesthonorar"]. "\n";
                        echo "" . $row["honorarkategorie"]. "\n";

                        echo "" . $row["von01"]. "\n";
                        echo "" . $row["bis01"]. "\n";

                        echo "" . $row["von02"]. "\n";
                        echo "" . $row["bis02"]. "\n";

                        echo "" . $row["hoerprobe01"]. "\n";
                        echo "" . $row["hoerprobe02"]. "\n";
                        echo "" . $row["hoerprobe03"]. "\n";

                        echo "" . $row["sa_kind"]. "\n";
                        echo "" . $row["sa_teenager"]. "\n";
                        echo "" . $row["sa_jungeerwachsen"]. "\n";
                        echo "" . $row["sa_bestejahre"]. "\n";
                        echo "" . $row["sa_seniorin"]. "\n";

                        echo "" . $row["sc_sonor"]. "\n";
                        echo "" . $row["sc_klar"]. "\n";
                        echo "" . $row["sc_rauh"]. "\n";
                        echo "" . $row["sc_weich"]. "\n";

                        echo "" . $row["sk_deutsch"]. "\n";
                        echo "" . $row["sk_englischgb"]. "\n";
                        echo "" . $row["sk_englischus"]. "\n";
                        echo "" . $row["sk_frz"]. "\n";
                        echo "" . $row["sk_ital"]. "\n";

                        echo "" . $row["sk_nied"]. "\n";
                        echo "" . $row["sk_pol"]. "\n";
                        echo "" . $row["sk_portu"]. "\n";
                        echo "" . $row["sk_russ"]. "\n";
                        echo "" . $row["sk_span"]. "\n";

                        echo "" . $row["sk_tuerk"]. "\n";

                        echo "" . $row["dl_bayerisch"]. "\n";
                        echo "" . $row["dl_berlinerisch"]. "\n";
                        echo "" . $row["dl_fraenkisch"]. "\n";
                        echo "" . $row["dl_hessisch"]. "\n";
                        echo "" . $row["dl_norddeutsch"]. "\n";

                        echo "" . $row["dl_rheinisch"]. "\n";
                        echo "" . $row["dl_saechsisch"]. "\n";
                        echo "" . $row["dl_schwaebisch"]. "\n";
                        echo "" . $row["dl_badisch"]. "\n";
                        echo "" . $row["dl_schweizerdeutsch"]. "\n";

                        echo "" . $row["dl_westfaelisch"]. "\n";
                        echo "" . $row["dl_wienerisch"]. "\n";

                        echo "" . $row["sl_hoch"]. "\n";
                        echo "" . $row["sl_mittel"]. "\n";
                        echo "" . $row["sl_tief"]. "\n";

                        echo "" . $row["ge_sachbuch"]. "\n";
                        echo "" . $row["ge_krimi"]. "\n";
                        echo "" . $row["ge_belle"]. "\n";
                        echo "" . $row["ge_erotik"]. "\n";

                        echo "" . $row["hp_beschreibung1"]. "\n";
                        echo "" . $row["hp_beschreibung2"]. "\n";
                        echo "" . $row["hp_beschreibung3"]. "\n";

                            

                 
                }
        } 
        else 
        {
                echo "0 results";
        }
        $conn->close();


?>