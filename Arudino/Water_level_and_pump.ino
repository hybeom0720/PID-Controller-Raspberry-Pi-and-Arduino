int Relaypin1 = 7;                 // IN1 
int Relaypin2 = 6;                 // IN2
 
void setup()
{
  Serial.begin(9600);
  pinMode(Relaypin1,OUTPUT);         // 릴레이 제어 1번핀을 출력으로 설정
  pinMode(Relaypin2,OUTPUT);         // 릴레이 제어 2번핀을 출력으로 설정
}
 
void loop()
{

  int level = analogRead(A0);
  Serial.println(level);
  if(level<500){
  digitalWrite (Relaypin1, LOW); // 릴레이 ON
               //1초 대기
  digitalWrite (Relaypin2, LOW); // 릴레이 OFF
  delay (100);            
  }
  else{
  digitalWrite (Relaypin1, HIGH);// 릴레이 ON             
  digitalWrite (Relaypin2, HIGH); // 릴레이 OFF
  delay (100);      
  }   
}
 
