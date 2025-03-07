package gherkinexecutor.Feature_Examples;
import java.util.*;
class TemperatureCalculation{
    String f = "0";
    String c = "0";
    String notes = "";
    public TemperatureCalculation() { }
    public TemperatureCalculation(
        String f
        ,String c
        ,String notes
        ){
        this.f = f;
        this.c = c;
        this.notes = notes;
        }
    @Override
    public boolean equals (Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass())
             return false;
        TemperatureCalculation _TemperatureCalculation = (TemperatureCalculation) o;
            boolean result = true;
         if (
             !this.f.equals("?DNC?")
                && !_TemperatureCalculation.f.equals("?DNC?"))
                if (! _TemperatureCalculation.f.equals(this.f)) result = false;
         if (
             !this.c.equals("?DNC?")
                && !_TemperatureCalculation.c.equals("?DNC?"))
                if (! _TemperatureCalculation.c.equals(this.c)) result = false;
         if (
             !this.notes.equals("?DNC?")
                && !_TemperatureCalculation.notes.equals("?DNC?"))
                if (! _TemperatureCalculation.notes.equals(this.notes)) result = false;
             return result;  }
    public static class Builder {
        private String f = "0";
        private String c = "0";
        private String notes = "";
        public Builder f(String f) {
            this.f = f;
            return this;
            }
        public Builder c(String c) {
            this.c = c;
            return this;
            }
        public Builder notes(String notes) {
            this.notes = notes;
            return this;
            }
        public Builder  setCompare() {
            f = "?DNC?";
            c = "?DNC?";
            notes = "?DNC?";
            return this;
            }
        public TemperatureCalculation build(){
             return new TemperatureCalculation(
                 f
                 ,c
                 ,notes
                );   } 
        } 
    @Override
    public String toString() {
        return "TemperatureCalculation {"
        +"f = " + f + " "
        +"c = " + c + " "
        +"notes = " + notes + " "
            + "} " + "\n"; }  
    public String toJson() {
        return " {"
        +""+"f:" + "\"" + f + "\""
        +","+"c:" + "\"" + c + "\""
        +","+"notes:" + "\"" + notes + "\""
            + "} " + "\n"; }  
        public static TemperatureCalculation fromJson(String json) {
              TemperatureCalculation instance = new TemperatureCalculation();

              	json = json.replaceAll("\\s", "");
                String[] keyValuePairs = json.replace("{", "").replace("}", "").split(",");

                // Iterate over the key-value pairs
                for (String pair : keyValuePairs) {
                    // Split each pair by the colon
                    String[] entry = pair.split(":");

                    // Remove the quotes from the key and value
                    String key = entry[0].replace("\"", "").trim();
                    String value = entry[1].replace("\"", "").trim();


          // Assign the value to the corresponding field
                    switch (key) {
              case "f":
                  instance.f = value;
                  break;
              case "c":
                  instance.c = value;
                  break;
              case "notes":
                  instance.notes = value;
                  break;
        				default:
        				    System.err.println("Invalid JSON element " + key);
                    }
                }
                return instance;
            }


             public static String listToJson(List<TemperatureCalculation> list) {
                 StringBuilder jsonBuilder = new StringBuilder();
                 jsonBuilder.append("[");

                 for (int i = 0; i < list.size(); i++) {
                     jsonBuilder.append(list.get(i).toJson());
                     if (i < list.size() - 1) {
                         jsonBuilder.append(",");
                     }
                 }

                 jsonBuilder.append("]");
                 return jsonBuilder.toString();
             }

             public static List<TemperatureCalculation> listFromJson(String json) {
                    List<TemperatureCalculation> list = new ArrayList<>();
            		json = json.replaceAll("\\s", "");
                    String[] jsonObjects = json.replace("[", "").replace("]", "").split("\\},\\{");

                    for (String jsonObject : jsonObjects) {
                        jsonObject = "{" + jsonObject.replace("{", "").replace("}", "") + "}";
                        list.add(TemperatureCalculation.fromJson(jsonObject));
                    }
                    return list;
                }

    TemperatureCalculationInternal toTemperatureCalculationInternal() {
        return new TemperatureCalculationInternal(
         Integer.valueOf(f)
        , Integer.valueOf(c)
        , notes
        ); }
    }
