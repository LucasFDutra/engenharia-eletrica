#define medicao A0

const unsigned char PS_16 = (1 << ADPS2);
const unsigned char PS_128 = (1 << ADPS2) | (1 << ADPS1) | (1 << ADPS0);

void setup() {
  Serial.begin(115200);
  ADCSRA &= ~PS_128; // Limpa a configuração previa
  ADCSRA |= PS_16;   // taxa de amostragem de 50K
}

void loop() {
  Serial.println(analogRead(medicao));
}
