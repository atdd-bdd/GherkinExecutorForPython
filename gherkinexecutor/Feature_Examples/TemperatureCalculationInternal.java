package gherkinexecutor.Feature_Examples;
import java.util.*;
class TemperatureCalculationInternal{
     Integer f;
     Integer c;
     String notes;
     
    public static String toDataTypeString() {
        return "TemperatureCalculationInternal {"
        +"Integer " 
        +"Integer " 
        +"String " 
            + "} "; }  
    TemperatureCalculation toTemperatureCalculation() {
        return new TemperatureCalculation(
        String.valueOf(f)
        ,String.valueOf(c)
        ,notes
        ); }
    public TemperatureCalculationInternal(
        Integer f
        ,Integer c
        ,String notes
        )  {
        this.f = f;
        this.c = c;
        this.notes = notes;
        }
    @Override
    public boolean equals (Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        TemperatureCalculationInternal _TemperatureCalculationInternal = (TemperatureCalculationInternal) o;
         return 
                ( _TemperatureCalculationInternal.f.equals(this.f))
                 && ( _TemperatureCalculationInternal.c.equals(this.c))
                 && ( _TemperatureCalculationInternal.notes.equals(this.notes))
             ;  }
    @Override
    public String toString() {
        return "TemperatureCalculationInternal {"
        +"f = " + f + " "
        +"c = " + c + " "
        +"notes = " + notes + " "
            + "} " + "\n"; }  
    }
