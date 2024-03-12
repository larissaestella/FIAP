/*
Código exemplo demonstrando o funcionamento do Sensor DTH11 enviando 
informações via serial no formato JSON para o servidor node-Red que recebe e transmite via protocolo MQTT 

*/

/////Json
#include <ArduinoJson.h>
const int TAMANHO = 50;  //define o tamanho do buffer para o json

///// Sensor DTH
#include "DHT.h"
#define DHTPIN  7  //define o pino usado no arduino
#define DHTTYPE DHT11
DHT dht(DHTPIN, DHTTYPE); //declara a objeto da classe

////// Outras declarações
#define led 13 //define led conectado no pino 13

void setup() 
{
  //inicialia c sensor
  dht.begin();

  //inicializa comunicação serial
  Serial.begin(9600);

  //configura pinos de saida do arduinos
  pinMode(led, OUTPUT);
}

void loop() 
{
  StaticJsonDocument<TAMANHO> json; //Aloca buffer para objeto json

  // Faz a leitura da temperatura  
  float temp = dht.readTemperature();
  // faz a leitura da humidade
  float umi = dht.readHumidity();

  //formato de escrita do json
  json["temperatura"] = temp;
  json["umidade"] = umi;

  serializeJson(json, Serial);
  Serial.println();

  //delay
  delay(500);
}
