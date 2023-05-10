{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter password to check: dfsf79889SDSA!@\n",
      "Password is adauite.\n"
     ]
    }
   ],
   "source": [
    "import re\n",
    "\n",
    "def check_password_strength(password):\n",
    "    \n",
    "    # Minimum password length\n",
    "    if len(password) < 12:\n",
    "        return \"Password should be at least 12 characters long, but 14 or more is better.\"\n",
    "\n",
    "    # Check for uppercase, lowercase, digits, and special characters\n",
    "    if not re.search(r\"[A-Z]\", password):\n",
    "        return \"Password should contain at least one uppercase letter.\"\n",
    "    if not re.search(r\"[a-z]\", password):\n",
    "        return \"Password should contain at least one lowercase letter.\"\n",
    "    if not re.search(r\"\\d\", password):\n",
    "        return \"Password should contain at least one digit.\"\n",
    "    if not re.search(r\"[ !#$%&'()*+,-./[\\\\\\]^_`{|}~\"\"]\", password):\n",
    "        return \"Password should contain at least one special character.\"\n",
    "    \n",
    "    # Password meets all criteria\n",
    "    return \"Password is suitable.\"\n",
    "\n",
    "if __name__ == '__main__':\n",
    "    password = input(\"Enter password to check: \")\n",
    "    strength = check_password_strength(password)\n",
    "    print(strength)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
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
   "version": "3.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
