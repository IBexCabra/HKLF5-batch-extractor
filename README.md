The program is intended to extract a specified batch to a HKLF4 type crystallographic hkl file from HKLF5 file. 
The next example makes it clear: 

Here is a fragment of an HKLF5 file (note that 1 and -2 are batch numbers): 
   0   0   3 86.8324 71.4505   1
   0   0   4 13430.9 112.800   1
  -3   0   5 41.6960 105.778  -2
   0   0   5 41.6960 105.778   1
   0   0  -6 886.362 89.7837   1
  -4   0   7 1078.04 97.2640  -2 
  
  The program, if run with parameters as follows -- progName input.hkl output.hkl batchNumber -- will save in output.hkl the next output, if the batchNumber is given a 1: 
  
     0   0   3 86.8324 71.4505
     0   0   4 13430.9 112.800
     0   0   5 41.6960 105.778
     0   0  -6 886.362 89.7837
	 
	 or, if the batchNumber is given as -2:
	 
    -3   0   5 41.6960 105.778
    -4   0   7 1078.04 97.2640

Any file types could be processed, if the batch number is limited by two numbers and separated by at least two spaces from the preceeding text. 

The program should help to extract quickly a batch into a HKLF4 formatted file, which should be handy for crystallographers, who work a lot with HKLF5 formatted data and would like to test the refinement against individual data batches. 

	
	
