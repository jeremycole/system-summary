A command to print a summary of hardware present in a system, using DMI information (from dmidecode) and proprietary system tools, if available.  On HP servers, if `Parse::HP:ACU` is installed from [perl-raid-tools](http://code.google.com/p/perl-raid-tools/), RAID information will be summarized as well.

# Examples #

## Dell PowerEdge 2950 ##

```
System Information:
  Model: Dell Inc. PowerEdge 2950
  Serial Number: 6C391C1

Processor Information:
  CPU1: Intel Xeon 3000 MHz, unknown cores
  CPU2: Intel Xeon 3000 MHz, unknown cores

Memory Information:
  DIMM1: 1024 MB, 533 MHz (1.9 ns)
  DIMM2: 1024 MB, 533 MHz (1.9 ns)
  DIMM3: 1024 MB, 533 MHz (1.9 ns)
  DIMM4: 1024 MB, 533 MHz (1.9 ns)
  DIMM5: Empty
  DIMM6: Empty
  DIMM7: Empty
  DIMM8: Empty
  Total Memory: 4096 MB
```

## Dell PowerEdge 860 ##

```
System Information:
  Model: Dell Computer Corporation PowerEdge 860
  Serial Number: JNRSGC1

Processor Information:
  PROC: Intel <OUT OF SPEC> 2800 MHz, unknown cores

Memory Information:
  DIMM1_A: 1024 MB, 533 MHz (1.9 ns)
  DIMM1_B: 1024 MB, 533 MHz (1.9 ns)
  DIMM2_A: Empty
  DIMM2_B: Empty
  Total Memory: 2048 MB
```

## HP DL360 G6 ##

```
System Information:
  Model: HP ProLiant DL360 G6
  Serial Number: XXXXXXXXXX

Processor Information:
  Proc 1: Intel <OUT OF SPEC> 2400 MHz, unknown cores
  Proc 2: Intel <OUT OF SPEC> 2400 MHz, unknown cores

Memory Information:
  PROC 1 DIMM 1: Empty
  PROC 1 DIMM 2: Empty
  PROC 1 DIMM 3: 2048 MB, 1333 MHz (0.8 ns)
  PROC 1 DIMM 4: Empty
  PROC 1 DIMM 5: Empty
  PROC 1 DIMM 6: 2048 MB, 1333 MHz (0.8 ns)
  PROC 1 DIMM 7: Empty
  PROC 1 DIMM 8: Empty
  PROC 1 DIMM 9: Empty
  PROC 2 DIMM 1: Empty
  PROC 2 DIMM 2: Empty
  PROC 2 DIMM 3: 2048 MB, 1333 MHz (0.8 ns)
  PROC 2 DIMM 4: Empty
  PROC 2 DIMM 5: Empty
  PROC 2 DIMM 6: 2048 MB, 1333 MHz (0.8 ns)
  PROC 2 DIMM 7: Empty
  PROC 2 DIMM 8: Empty
  PROC 2 DIMM 9: Empty
  Total Memory: 8192 MB

Storage Controller 1: HP Smart Array P410i in Slot 0 (Embedded), 1 arrays, OK
  Cache: 256 MB, 100%/0%, BBWC , OK
  Array A: SAS, 1 logical, 2 physical, OK
    Logical Drive 1: c0d0, 136.7 GB, RAID 1, 128 KB stripe, write back, OK
      Mirror Group 0: 1I:1:1
      Mirror Group 1: 1I:1:2
    Physical Drive 1I:1:1: SAS, 146 GB, 15.0k RPM, OK
    Physical Drive 1I:1:2: SAS, 146 GB, 15.0k RPM, OK
```

## HP DL380 G6 ##

```
System Information:
  Model: HP ProLiant DL380 G6
  Serial Number: XXXXXXXXXX

Processor Information:
  Proc 1: Intel <OUT OF SPEC> 2400 MHz, unknown cores
  Proc 2: Intel <OUT OF SPEC> 2400 MHz, unknown cores

Memory Information:
  PROC 1 DIMM 1G: Empty
  PROC 1 DIMM 2D: 2048 MB, 1333 MHz (0.8 ns)
  PROC 1 DIMM 3A: 2048 MB, 1333 MHz (0.8 ns)
  PROC 1 DIMM 4H: Empty
  PROC 1 DIMM 5E: 2048 MB, 1333 MHz (0.8 ns)
  PROC 1 DIMM 6B: 2048 MB, 1333 MHz (0.8 ns)
  PROC 1 DIMM 7I: Empty
  PROC 1 DIMM 8F: 2048 MB, 1333 MHz (0.8 ns)
  PROC 1 DIMM 9C: 2048 MB, 1333 MHz (0.8 ns)
  PROC 2 DIMM 1G: Empty
  PROC 2 DIMM 2D: 2048 MB, 1333 MHz (0.8 ns)
  PROC 2 DIMM 3A: 2048 MB, 1333 MHz (0.8 ns)
  PROC 2 DIMM 4H: Empty
  PROC 2 DIMM 5E: 2048 MB, 1333 MHz (0.8 ns)
  PROC 2 DIMM 6B: 2048 MB, 1333 MHz (0.8 ns)
  PROC 2 DIMM 7I: Empty
  PROC 2 DIMM 8F: 2048 MB, 1333 MHz (0.8 ns)
  PROC 2 DIMM 9C: 2048 MB, 1333 MHz (0.8 ns)
  Total Memory: 24576 MB

Storage Controller 1: HP Smart Array P410i in Slot 0 (Embedded), 2 arrays, OK
  Cache: 512 MB, 25%/75%, BBWC OK, OK
  Array A: SAS, 1 logical, 2 physical, OK
    Logical Drive 1: c0d0, 136.7 GB, RAID 1, 128 KB stripe, write back, OK
      Mirror Group 0: 2C:1:1
      Mirror Group 1: 4C:2:1
    Physical Drive 2C:1:1: SAS, 146 GB, 15.0k RPM, OK
    Physical Drive 4C:2:1: SAS, 146 GB, 15.0k RPM, OK
  Array B: SAS, 1 logical, 6 physical, OK
    Logical Drive 2: c0d1, 410.1 GB, RAID 1+0, 128 KB stripe, write back, OK
      Mirror Group 0: 2C:1:2, 3C:1:5, 3C:1:6
      Mirror Group 1: 4C:2:2, 5C:2:5, 5C:2:6
    Physical Drive 2C:1:2: SAS, 146 GB, 15.0k RPM, OK
    Physical Drive 3C:1:5: SAS, 146 GB, 15.0k RPM, OK
    Physical Drive 3C:1:6: SAS, 146 GB, 15.0k RPM, OK
    Physical Drive 4C:2:2: SAS, 146 GB, 15.0k RPM, OK
    Physical Drive 5C:2:5: SAS, 146 GB, 15.0k RPM, OK
    Physical Drive 5C:2:6: SAS, 146 GB, 15.0k RPM, OK
```

## HP DL360 G5 ##

```
System Information:
 Model: HP ProLiant DL360 G5
 Serial Number: XXXXXXXXXX

Processor Information:
 Proc 1: Intel Xeon 1866 MHz, unknown cores
 Proc 2: Intel Xeon 1866 MHz, unknown cores

Memory Information:
 DIMM 1A: 4096 MB, 667 MHz (1.5 ns)
 DIMM 2C: Empty
 DIMM 3A: 4096 MB, 667 MHz (1.5 ns)
 DIMM 4C: Empty
 DIMM 5B: 4096 MB, 667 MHz (1.5 ns)
 DIMM 6D: Empty
 DIMM 7B: 4096 MB, 667 MHz (1.5 ns)
 DIMM 8D: Empty
 Total Memory: 16384 MB

Storage Controller 1: HP Smart Array P400i in Slot 0 (Embedded), 1 arrays, OK
 Cache: 512 MB, 25%/75%, BBWC OK, OK
 Array A: SAS, 1 logical, 3 physical, OK
   Logical Drive 1: c0d0, 136.7 GB, RAID 1, 128 KB stripe, write back, OK
     Mirror Group 0: 1I:1:1
     Mirror Group 1: 1I:1:2
   Physical Drive 1I:1:1: SAS, 146 GB, 10.0k RPM, OK
   Physical Drive 1I:1:2: SAS, 146 GB, 10.0k RPM, OK
   Physical Drive 1I:1:3: SAS, 146 GB, 10.0k RPM, OK
```

## HP DL180 G5 ##

```
System Information:
 Model: HP ProLiant DL180 G5
 Serial Number: XXXXXXXXXX

Processor Information:
 CPU 0: Intel Xeon MP 1866 MHz, unknown cores
 CPU 1: Intel Xeon MP 1866 MHz, unknown cores

Memory Information:
 DIMM1 A: 2048 MB, 667 MHz (1.5 ns)
 DIMM2 A: 2048 MB, 667 MHz (1.5 ns)
 DIMM3 B: Empty
 DIMM4 B: Empty
 DIMM5 C: Empty
 DIMM6 C: Empty
 Total Memory: 4096 MB

Storage Controller 1: HP Smart Array P400 in Unknown Slot, 1 arrays, OK
 Cache: 256 MB, 25%/75%, BBWC OK, OK
 Array A: SAS, 1 logical, 3 physical, OK
   Logical Drive 1: c0d0, 136.7 GB, RAID 1, 128 KB stripe, write back, OK
     Mirror Group 0: 1I:1:1
     Mirror Group 1: 1I:1:2
   Physical Drive 1I:1:1: SAS, 146 GB, 15.0k RPM, OK
   Physical Drive 1I:1:2: SAS, 146 GB, 15.0k RPM, OK
   Physical Drive 1I:1:3: SAS, 146 GB, 15.0k RPM, OK
```

## Shuttle SK48 ##

```
System Information:
  Model: Shuttle Inc SK48
  Serial Number: 0

Processor Information:
  Socket 775: Intel <OUT OF SPEC> 2000 MHz, unknown cores

Memory Information:
  A0: 1024 MB, Unknown
  A1: Empty
  A2: 1024 MB, Unknown
  A3: Empty
  Total Memory: 2048 MB
```

## HP Pavilion m9500f ##

```
System Information:
  Model: HP-Pavilion FQ562AA-ABA m9500f
  Serial Number: XXXXXXXXXX

Processor Information:
  Socket AM2: AMD Athlon 64 X2 2400 MHz, 4 cores

Memory Information:
  A0: 2048 MB, 800 MHz
  A1: 2048 MB, 800 MHz
  A2: 2048 MB, 800 MHz
  A3: 2048 MB, 800 MHz
  Total Memory: 8192 MB
```