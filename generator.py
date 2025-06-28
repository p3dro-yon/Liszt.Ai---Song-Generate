from midiutil import MIDIFile
import random

def generate_piano_midi(
        output_file="piano_music.mid",
        num_measures=4,
        tempo=120,
        key="C",
        scale_type="major"
    ):

    # Configurações iniciais
    track = 0 # Pista MIDI
    channel = 0 # Canal
    time = 0    # Tempo inicial
    duration = 1 # Duração das notas
    volume = 100 # Volume

    midi = MIDIFile(1)
    midi.addTempo(track, time, tempo)

    # Escalas (notas em semitons)
    scales = {
        "major": [0, 2, 4, 5, 7, 9, 11],
        "minor": [0, 2, 3, 5, 7, 8, 10],
        "blues": [0, 3, 5, 6, 7, 10]
    }
    
    # Notas base por tom
    base_notes = {"C": 60, "D": 62, "E": 64, "F": 65, "G": 67, "A": 69, "B": 71}
    base_note = base_notes[key]
    
    for measure in range(num_measures):
        for beat in range(4):  # Tempo por compasso
            if random.random() > 0.3:  # Chance de tocar uma nota
                note_offset = random.choice(scales[scale_type])
                note = base_note + note_offset + random.choice([0, 12])  # Oitavas
                
                midi.addNote(track, channel, note, time, duration, volume)
            time += duration

    with open(output_file, "wb") as f:
        midi.writeFile(f)
    print(f": {output_file}")

if __name__ == "__main__":
    # Exemplo de uso
    generate_piano_midi("exemplo1.mid")
    generate_piano_midi("exemplo2.mid", num_measures=8, tempo=90, key="G", scale_type="blues")
