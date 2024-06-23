#pragma once
#include <iostream> // input output ���� ���
#include <string>   // ���ڿ� 
#include <vector>
using namespace std;    //std ���̺귯�� namespace ����

// SmartHome
class SmartHome {
private:
    // Ŭ���� ������ (member variable, attribute, field)
    string owner;  // ���ڿ�
    int temperature;    // ������
    int humidity;
    bool security; // true or false
public:
    // Ŭ���� �Լ��� (member function, method)
    // ������
    SmartHome(string owner, int temperature, int humidity, bool security) {
        this->owner = owner;
        this->temperature = temperature;
        this->humidity = humidity;
        this->security = security;
    }
    // Parameter , Argument
    //SmartHome(string o, int t, int h, bool sec)
    //    : temperature(t), humidity(h), security(sec) {
    //    strcpy(owner, o);
    //}
 
    // �Ҹ���
    ~SmartHome() {}

    void setTemperature(int temperature) {
        this->temperature = temperature;
    }
    void setHumidity(int humidity) {
        this->humidity = humidity;
    }
    void setSecurity(bool security) {
        this->security = security;
    }
    string getOwner() {
        return this->owner;
    }
    int getTemperature() {
        return this->temperature;
    }
    int getHumidity() {
        return this->humidity;
    }
    bool getSecurity() {
        return this->security;
    }
    void printStatus() {
        cout << "������: " << this->owner << endl;
        cout << "�µ�: " << this->temperature << "��" << endl;
        cout << "����: " << this->humidity << "%" << endl;
        if (this->security) {
            cout << " security on" << endl;
        }
        else {
            cout << "security off" << endl;
        }
    }
};