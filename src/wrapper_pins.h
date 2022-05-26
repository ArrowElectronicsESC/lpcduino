#ifndef _WRAPPER_PINS_H_
#define _WRAPPER_PINS_H_

#ifdef __cplusplus
extern "C" {
#endif

#include <stdint.h>

#define LED_BUILTIN (17)

typedef enum pin_mode {
    INPUT = 0,
    OUTPUT,
} pin_mode_t;

typedef enum pin_level {
    LOW = 0,
    HIGH,
} pin_level_t;

void pinMode(uint8_t pin, pin_mode_t mode);
void digitalWrite(uint8_t pin, pin_level_t level);

#ifdef __cplusplus
}
#endif

#endif
