#include <gtk/gtk.h>
#include <stdio.h>

int main(void) {
    gtk_init();
    GtkWidget *view = gtk_text_view_new();
    g_object_ref_sink(view);
    GtkTextBuffer *buffer = gtk_text_view_get_buffer(GTK_TEXT_VIEW(view));
    gtk_text_buffer_set_text(buffer, "α", -1);
    if (gtk_text_buffer_get_char_count(buffer) != 1) return 1;
    printf("GTK control bootstrap: 1 passed, 0 failed; GTK %u.%u.%u\n",
           gtk_get_major_version(), gtk_get_minor_version(), gtk_get_micro_version());
    g_object_unref(view);
    return 0;
}
