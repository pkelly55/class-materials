## Table

```markdown

Input Data : 6 7 4 0 9 3 1 8 2 5
Output Data: 0 1 2 3 4 5 6 7 8 9

							QS(0,9) 
		      QS(0,4)		           QS(6,9)
	QS(0,1)           QS(3,4)      QS(6,5)      QS(7,9)
QS(0,0)  QS(2,1)   QS(3,2) QS(4,4)        QS(7,6)   QS(8,9)
                                               QS(8,7)  QS(9,9)   


QS(0,9)		[4 0 3 1 2 5 7 8 9 6]
QS(0,4)		[0 1 2 4 3 5 7 8 9 6]
QS(6,9)		[0 1 2 4 3 5 6 8 9 7]
QS(0,1)		[0 1 2 4 3 5 6 8 9 7]
QS(3,4)		[0 1 2 3 4 5 6 8 9 7]
QS(6,5)		[0 1 2 4 3 5 6 8 9 7]
QS(7,9)		[0 1 2 3 4 5 6 7 9 8]
QS(0,0)     [0 1 2 4 3 5 6 8 9 7]
QS(2,1)     [0 1 2 4 3 5 6 8 9 7]
QS(3,2)		[0 1 2 3 4 5 6 8 9 7]
QS(4,4)		[0 1 2 3 4 5 6 8 9 7]
QS(7,6)		[0 1 2 3 4 5 6 7 9 8]
QS(8,9)		[0 1 2 3 4 5 6 7 8 9]
QS(8,7)		[0 1 2 3 4 5 6 7 8 9]
QS(9,9)		[0 1 2 3 4 5 6 7 8 9]



```