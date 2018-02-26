text = "X-DSPAM-Confidence:    0.8475";
y=text.find('0')
print(float(text[y:]))