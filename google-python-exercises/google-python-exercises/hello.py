text = "X-DSPAM-Confidence:    0.8475";
new_text = text.strip()
pos = new_text.find('0')
num_str = new_text[pos:]
print(float(num_str))