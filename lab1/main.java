import javax.swing.*;
import java.awt.*;
 
class ColorConverter extends JFrame {
 
    private JColorChooser colorChooser;
 
    private JLabel infoLabel;
 
    public ColorConverter() {
        super("Color converter");
        setSize(600, 400);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
 
        colorChooser = new JColorChooser();
        add(colorChooser, BorderLayout.CENTER);
 
        JPanel labelsPanel = new JPanel();
        infoLabel = new JLabel();
        labelsPanel.add(infoLabel);
        add(labelsPanel, BorderLayout.SOUTH);
 
        colorChooser.getSelectionModel().addChangeListener(e -> updateColors());
        setVisible(true);
    }
 
    private void updateColors() {
        Color col = colorChooser.getColor();
 
        infoLabel.setText("RGB: " + col.getRed() + ", " + col.getGreen() + ", " + col.getBlue());
 
        infoLabel.setText(infoLabel.getText() + " CMYK: " + (int)((1 - (float)col.getRed() / 255)*100) + ", " +
                (int)((1 - (float)col.getGreen() / 255)*100) + ", " +
                (int)((1 - (float)col.getBlue() / 255)*100) + ", " +
                (int)((1 - Math.max(Math.max(1 - (float)col.getRed() / 255, 1 - (float)col.getGreen() / 255), (1 - (float)col.getBlue() / 255)))*100));
 
        float[] hsv = Color.RGBtoHSB(col.getRed(), col.getGreen(), col.getBlue(), null);
        infoLabel.setText(infoLabel.getText() + " HSV: " + (int)(hsv[0] * 360) + ", " + (int)(hsv[1] * 100) + ", " + (int)(hsv[2] * 100));
    }
 
    public static void main(String[] args) {
        new ColorConverter();
    }
}
