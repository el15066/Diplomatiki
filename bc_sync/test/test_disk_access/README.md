# Specifications
TODO

## Εκτέλεση/καταγραφή 3

Καταγραφή των synchronous writes στο σύστημα αρχείων (`vfs_write()`) κατά το Execution stage.

[Log](data/exec3.log)

#### Θέσεις εγγραφής

Οριζόντιος άξονας: αριθμός του request  
Κατακόρυφος: θέση στο vfs (σε block, 1 block = 4096 B)

![](img/Write_positions.png)
zoom
![](img/Write_positions_zoom1.png)
zoom
![](img/Write_positions_zoom2.png)
zoom
![](img/Write_positions_zoom3.png)

#### Θέσεις εγγραφής ως προς χρόνο

Οριζόντιος άξονας: wall time (s)  
Κατακόρυφος: θέση στο vfs (σε block, 1 block = 4096 B)

![](img/Write_pos_over_time.png)
zoom
![](img/Write_pos_over_time_zoom1.png)
zoom
![](img/Write_pos_over_time_zoom2.png)

#### Χρόνος σε εγγραφές ως προς συνολικό χρόνο

Οριζόντιος άξονας: wall time (s)  
Κατακόρυφος: time spent writing

![](img/Sum_dt_over_time.png)
zoom
![](img/Sum_dt_over_time_zoom1.png)
zoom
![](img/Sum_dt_over_time_zoom2.png)
zoom
![](img/Sum_dt_over_time_zoom3.png)
