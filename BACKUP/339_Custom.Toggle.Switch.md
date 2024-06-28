# [Custom Toggle Switch](https://github.com/platojobs/SFLOG/issues/339)

```swift
import SwiftUI

struct CustomToggle: View {
    @Binding var isOn: Bool
    var onColor: Color = .green
    var offColor: Color = .red

    var body: some View {
        HStack {
            RoundedRectangle(cornerRadius: 16)
                .fill(isOn ? onColor : offColor)
                .frame(width: 50, height: 30)
                .overlay(
                    Circle()
                        .fill(Color.white)
                        .frame(width: 24, height: 24)
                        .offset(x: isOn ? 10 : -10)
                        .animation(.default, value: isOn)
                )
                .onTapGesture {
                    isOn.toggle()
                }
            Text(isOn ? "ON" : "OFF")
                .font(.headline)
                .padding(.leading, 10)
        }
        .padding()
    }
}

struct CustomToggle_Previews: View {
    @State private var isOn = true

    var body: some View {
        Group {
            CustomToggle(isOn: $isOn)
                .previewDisplayName("ON State")

            CustomToggle(isOn: .constant(false))
                .previewDisplayName("OFF State")
        }
    }
}

#Preview {
    CustomToggle_Previews()
}

```