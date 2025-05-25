{{- define "users-api.name" -}}
{{ .Chart.Name }}
{{- end }}

{{- define "users-api.fullname" -}}
{{ .Chart.Name }}
{{- end }}

{{- define "users-api.serviceAccountName" -}}
{{- if .Values.serviceAccount.create }}
{{ include "users-api.fullname" . }}
{{- else }}
default
{{- end }}
{{- end }}

{{- define "users-api.labels" -}}
app.kubernetes.io/name: {{ include "users-api.name" . }}
app.kubernetes.io/instance: {{ .Release.Name }}
{{- end }}
