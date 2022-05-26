#include "LPC8xx.h"
#include "wrapper_pins.h"

void pinMode(uint8_t pin, pin_mode_t mode) {  
    LPC_GPIO_PORT->DIR0 |= (mode << pin);
}

void digitalWrite(uint8_t pin, pin_level_t level) {
    if (level == HIGH) {
        LPC_GPIO_PORT->SET0 = 1 << pin;
    } else {
        LPC_GPIO_PORT->CLR0 = 1 << pin;
    }
}
