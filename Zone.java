public class Zone {
    private int spaces,
                disc_spaces;
    private tuplet[] connections;
    
    public Zone(int spaces, int disc_spaces, int preg_spaces, tuplet[] connections) {
        
    }
    
    public void Output(int e) {
        DB.push(tuplet[e]);
        
    }
}

public class InputZone extends Zone {
    private Sensor[] input;
    
    
}