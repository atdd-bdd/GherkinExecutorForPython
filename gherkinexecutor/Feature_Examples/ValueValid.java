package gherkinexecutor.Feature_Examples;
import java.util.*;
class ValueValid{
    String value = "0";
    String valid = "false";
    String notes = "";
    public ValueValid() { }
    public ValueValid(
        String value
        ,String valid
        ,String notes
        ){
        this.value = value;
        this.valid = valid;
        this.notes = notes;
        }
    @Override
    public boolean equals (Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass())
             return false;
        ValueValid _ValueValid = (ValueValid) o;
            boolean result = true;
         if (
             !this.value.equals("?DNC?")
                && !_ValueValid.value.equals("?DNC?"))
                if (! _ValueValid.value.equals(this.value)) result = false;
         if (
             !this.valid.equals("?DNC?")
                && !_ValueValid.valid.equals("?DNC?"))
                if (! _ValueValid.valid.equals(this.valid)) result = false;
         if (
             !this.notes.equals("?DNC?")
                && !_ValueValid.notes.equals("?DNC?"))
                if (! _ValueValid.notes.equals(this.notes)) result = false;
             return result;  }
    public static class Builder {
        private String value = "0";
        private String valid = "false";
        private String notes = "";
        public Builder value(String value) {
            this.value = value;
            return this;
            }
        public Builder valid(String valid) {
            this.valid = valid;
            return this;
            }
        public Builder notes(String notes) {
            this.notes = notes;
            return this;
            }
        public Builder  setCompare() {
            value = "?DNC?";
            valid = "?DNC?";
            notes = "?DNC?";
            return this;
            }
        public ValueValid build(){
             return new ValueValid(
                 value
                 ,valid
                 ,notes
                );   } 
        } 
    @Override
    public String toString() {
        return "ValueValid {"
        +"value = " + value + " "
        +"valid = " + valid + " "
        +"notes = " + notes + " "
            + "} " + "\n"; }  
    public String toJson() {
        return " {"
        +""+"value:" + "\"" + value + "\""
        +","+"valid:" + "\"" + valid + "\""
        +","+"notes:" + "\"" + notes + "\""
            + "} " + "\n"; }  
        public static ValueValid fromJson(String json) {
              ValueValid instance = new ValueValid();

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
              case "value":
                  instance.value = value;
                  break;
              case "valid":
                  instance.valid = value;
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


             public static String listToJson(List<ValueValid> list) {
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

             public static List<ValueValid> listFromJson(String json) {
                    List<ValueValid> list = new ArrayList<>();
            		json = json.replaceAll("\\s", "");
                    String[] jsonObjects = json.replace("[", "").replace("]", "").split("\\},\\{");

                    for (String jsonObject : jsonObjects) {
                        jsonObject = "{" + jsonObject.replace("{", "").replace("}", "") + "}";
                        list.add(ValueValid.fromJson(jsonObject));
                    }
                    return list;
                }

    ValueValidInternal toValueValidInternal() {
        return new ValueValidInternal(
         value
        , Boolean.parseBoolean(valid)
        , notes
        ); }
    }
