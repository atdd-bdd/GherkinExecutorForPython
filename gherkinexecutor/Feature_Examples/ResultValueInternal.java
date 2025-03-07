package gherkinexecutor.Feature_Examples;
import java.util.*;
class ResultValueInternal{
     Integer sum;
     
    public static String toDataTypeString() {
        return "ResultValueInternal {"
        +"Integer " 
            + "} "; }  
    ResultValue toResultValue() {
        return new ResultValue(
        String.valueOf(sum)
        ); }
    public ResultValueInternal(
        Integer sum
        )  {
        this.sum = sum;
        }
    @Override
    public boolean equals (Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        ResultValueInternal _ResultValueInternal = (ResultValueInternal) o;
         return 
                ( _ResultValueInternal.sum.equals(this.sum))
             ;  }
    @Override
    public String toString() {
        return "ResultValueInternal {"
        +"sum = " + sum + " "
            + "} " + "\n"; }  
    }
