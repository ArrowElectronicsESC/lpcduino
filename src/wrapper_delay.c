#include "LPC8xx.h"
#include "wrapper_delay.h"
#include "mrt.h"

#define TEST_DEFINE 100
void delay(uint32_t millisec){
    mrtDelay(millisec);
}