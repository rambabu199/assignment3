{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "9907c2cd",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "No. of Upper case characters: 3\n",
      "No. of lower case characters: 12\n"
     ]
    }
   ],
   "source": [
    "'''a Python function that accepts a string and \n",
    "calculate the number of upper case letters and lower case letters.'''\n",
    "string1='The quick Brow Fox' #sample string\n",
    "dict1={\"u1\":0,\"l1\":0}\n",
    "def cal_up_low(str1):  #function for caluculate the upper & lower cases in string\n",
    "    for i in string1:\n",
    "        if i.isupper():\n",
    "            dict1['u1']+=1\n",
    "        elif i.islower():\n",
    "            dict1['l1']+=1\n",
    "        else:\n",
    "            pass\n",
    "    return dict1\n",
    "calc=cal_up_low(string1)\n",
    "print(\"No. of Upper case characters:\",dict1[\"u1\"])\n",
    "print(\"No. of lower case characters:\",dict1[\"l1\"])\n",
    "        "
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
