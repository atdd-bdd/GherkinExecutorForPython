package gherkinexecutor.Feature_Examples;
import java.util.*;
class ValueValidInternal{
     String value;
     Boolean valid;
     String notes;
     
    public static String toDataTypeString() {
        return "ValueValidInternal {"
        +"String " 
        +"Boolean " 
        +"String " 
            + "} "; }  
    ValueValid toValueValid() {
        return new ValueValid(
        value
        ,String.valueOf(valid)
        ,notes
        ); }
    public ValueValidInternal(
        String value
        ,Boolean valid
        ,String notes
        )  {
        this.value = value;
        this.valid = valid;
        this.notes = notes;
        }
    @Override
    public boolean equals (Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        ValueValidInternal _ValueValidInternal = (ValueValidInternal) o;
         return 
                ( _ValueValidInternal.value.equals(this.value))
                 && ( _ValueValidInternal.valid.equals(this.valid))
                 && ( _ValueValidInternal.notes.equals(this.notes))
             ;  }
    @Override
    public String toString() {
        return "ValueValidInternal {"
        +"value = " + value + " "
        +"valid = " + valid + " "
        +"notes = " + notes + " "
            + "} " + "\n"; }  
    }
