package gherkinexecutor.Feature_Examples;

import java.util.ArrayList;
import java.util.List;


public class SolutionForListOfNumber {
    private final List<LabelValueInternal> values = new ArrayList <>();
    private ID filterValue = new ID("Q0000");
    void add(LabelValueInternal value) {
        values.add(value);
    }

    void setFilterValue(ID value) {
        filterValue = value;
    }

    int sum(){
        var sum = 0;
        for (LabelValueInternal element : values) {
            if (element.iD.equals(filterValue))
                sum += (element.value);
        }
        return sum;
    }
}
