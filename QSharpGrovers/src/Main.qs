namespace GraphColoring {
    open Microsoft.Quantum.Canon;
    open Microsoft.Quantum.Intrinsic;
    open Microsoft.Quantum.Arrays;
    open Microsoft.Quantum.Diagnostics;

    operation Main() : Unit {
        let states = ["Alabama", "Alaska", "Arizona", "Arkansas", "California", 
                      "Colorado", "Connecticut", "Delaware", "Florida", "Georgia",
                      "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa",
                      "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland",
                      "Massachusetts", "Michigan", "Minnesota", "Mississippi", "Missouri",
                      "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey",
                      "New Mexico", "New York", "North Carolina", "North Dakota", "Ohio",
                      "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island", "South Carolina",
                      "South Dakota", "Tennessee", "Texas", "Utah", "Vermont",
                      "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming"];
        
        let neighbors = [
            [8, 9, 23, 41], // Alabama
            [], // Alaska
            [4, 5, 27, 30, 43], // Arizona
            [17, 23, 24, 35, 41, 42], // Arkansas
            [2, 27, 36], // California
            [2, 15, 26, 30, 35, 43, 49], // Colorado
            [6, 20, 31, 38], // Connecticut
            [19, 29, 37], // Delaware
            [0, 9], // Florida
            [0, 8, 32, 39, 41], // Georgia
            [], // Hawaii
            [25, 27, 36, 43, 46, 49], // Idaho
            [13, 14, 21, 16, 24, 48], // Illinois
            [12, 16, 21, 34], // Indiana
            [12, 22, 24, 26, 40, 48], // Iowa
            [5, 24, 26, 35], // Kansas
            [12, 13, 24, 34, 41, 45, 47], // Kentucky
            [3, 23, 42], // Louisiana
            [28], // Maine
            [7, 37, 45, 47], // Maryland
            [6, 28, 31, 38, 44], // Massachusetts
            [12, 13, 22, 34, 48], // Michigan
            [14, 21, 33, 40, 48], // Minnesota
            [0, 3, 17, 41], // Mississippi
            [3, 12, 14, 15, 16, 26, 35, 41], // Missouri
            [11, 33, 40, 49], // Montana
            [5, 14, 15, 24, 40, 49], // Nebraska
            [2, 4, 11, 36, 43], // Nevada
            [18, 20, 44], // New Hampshire
            [7, 31, 37], // New Jersey
            [2, 5, 35, 42, 43], // New Mexico
            [6, 20, 29, 37, 38, 44], // New York
            [9, 39, 41, 45], // North Carolina
            [22, 25, 40], // North Dakota
            [13, 16, 21, 37, 47], // Ohio
            [3, 5, 15, 24, 30, 42], // Oklahoma
            [4, 11, 27, 46], // Oregon
            [7, 19, 29, 31, 34, 47], // Pennsylvania
            [6, 20, 31], // Rhode Island
            [9, 32], // South Carolina
            [14, 22, 25, 26, 33, 49], // South Dakota
            [0, 3, 9, 16, 23, 24, 32, 45], // Tennessee
            [3, 17, 30, 35], // Texas
            [2, 5, 11, 27, 30, 49], // Utah
            [20, 28, 31], // Vermont
            [16, 19, 32, 41, 47], // Virginia
            [11, 36], // Washington
            [16, 19, 34, 37, 45], // West Virginia
            [12, 14, 21, 22], // Wisconsin
            [5, 11, 25, 26, 40, 43] // Wyoming
        ];

        use qs = Qubit[3];
        Grovers(qs);

        let colors = ["red", "green", "blue", "yellow"];
        let coloring = ColorStates(neighbors, Length(colors));
        let isValid = ValidateColoring(neighbors, coloring);

        for i in 0..Length(states)-1 {
            Message($"{states[i]}: {colors[coloring[i]]}");
        }
    }

    operation Grovers(qs : Qubit[]) : Unit {
        for qubit in qs {
            H(qubit);
        }
        Oracle(qs);
        Diffuser(qs);
    }

    operation Oracle(qs : Qubit[]) : Unit is Adj {
        within {
            for qubit in qs {
                X(qubit);
            }
        } apply {
            Z(qs[0]);
            for qubit in qs {
                X(qubit);
            }
        }
    }

    operation Diffuser(qs : Qubit[]) : Unit is Adj {
        within {
            for qubit in qs {
                H(qubit);
            }
            for qubit in qs {
                X(qubit);
            }
        } apply {
            Controlled Z(Most(qs), Tail(qs));
            for qubit in qs {
                X(qubit);
            }
            for qubit in qs {
                H(qubit);
            }
        }
    }

    function ValidateColoring(neighbors : Int[][], coloring : Int[]) : Bool {
        for i in 0..Length(neighbors)-1 {
            for neighbor in neighbors[i] {
                if coloring[i] == coloring[neighbor] {
                    return false;
                }
            }
        }
        return true;
    }

    function IsSafe(state : Int, color : Int, coloring : Int[], neighbors : Int[][]) : Bool {
        for neighbor in neighbors[state] {
            if coloring[neighbor] != -1 and coloring[neighbor] == color {
                return false;
            }
        }
        return true;
    }

    function ColorStatesAux(neighbors : Int[][], numColors : Int, coloring : Int[], index : Int) : (Bool, Int[]) {
        if index == Length(neighbors) {
            return (true, coloring);
        }

        for color in 0..numColors-1 {
            if IsSafe(index, color, coloring, neighbors) {
                let newColoring = coloring w/ index <- color;
                let (success, resultColoring) = ColorStatesAux(neighbors, numColors, newColoring, index + 1);
                if success {
                    return (true, resultColoring);
                }
            }
        }
        return (false, coloring);
    }

    function ColorStates(neighbors : Int[][], numColors : Int) : Int[] {
        let initialColoring = [-1, size = Length(neighbors)];
        let (success, coloring) = ColorStatesAux(neighbors, numColors, initialColoring, 0);
        if not success {
            fail "No valid coloring found";
        }
        return coloring;
    }
}