{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "4231bbf5",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "4321dcba\n"
     ]
    }
   ],
   "source": [
    "''' Python program to reverse a string.''' \n",
    "string1='abcd1234'  #sample string\n",
    "def rev_str(str1):  # single argument function\n",
    "    str1=string1[::-1]# reversing the string by using slicing techniq\n",
    "    return str1 # returning a value\n",
    "str2=rev_str(string1) # calling the function \n",
    "print(str2) # printing the reverse string"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
