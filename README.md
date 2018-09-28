# sogis-ili-repo

## Import/Export
```
java -jar /Users/stefan/apps/ili2pg-3.11.2/ili2pg.jar --dbhost 192.168.50.8 --dbdatabase pub --dbusr ddluser --dbpwd ddluser --nameByTopic --createEnumTabs --beautifyEnumDispName --createFk --createFkIdx --createNumChecks --createUnique --models IliRepository09 --dbschema agi_ilirepository --schemaimport
```

Import bestehendes ilimodels.xml (löscht bestehende Daten in DB):
```
java -jar /Users/stefan/apps/ili2pg-3.11.2/ili2pg.jar --dbhost 192.168.50.8 --dbdatabase pub --dbusr ddluser --dbpwd ddluser --nameByTopic --createEnumTabs --beautifyEnumDispName --createFk --createFkIdx --createNumChecks --createUnique --models IliRepository09 --dbschema agi_ilirepository --deleteData --import ilimodels.xml
```

Export nach ilimodels.xml:
```
java -jar /Users/stefan/apps/ili2pg-3.11.2/ili2pg.jar --dbhost 192.168.50.8 --dbdatabase pub --dbusr ddluser --dbpwd ddluser --nameByTopic --createEnumTabs --beautifyEnumDispName --createFk --createFkIdx --createNumChecks --createUnique --models IliRepository09 --dbschema agi_ilirepository --export ilimodels2.xml
```


## QGIS

* Filedialog ("Attachement") muss so eingestellt sein, dass der relative Pfad in der DB gespeichert wird. Dieser muss dann dem Pfad im Web entsprechen ("AGI/DM01.ili").

* md5-Checksumme:


## Build
docker run -it  --rm --name some-nginx -d -p 8080:80 some-content-nginx

Fragen:
* "schöne" TID aufgeben? Mehrwert? Sind aber mühsam zum Verwalten / bei der Vergabe.